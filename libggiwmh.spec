%define major 0
%define libname %mklibname ggiwmh %{major}
%define develname %mklibname -d ggiwmh
%define staticname %mklibname -s -d ggiwmh

Summary:	Extension to libggi whereby wmh stands for 'Window Manager Hints'
Name:		libggiwmh
Version:	0.3.2
Release:	%mkrel 4
License:        BSD
Group:		System/Libraries
Url:		http://www.ggi-project.org
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libggi-devel	>= 2.2.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
It adds features like moving, resizing, iconifying, z-ordering 
Windows and more that happen to contain a ggi visual. It is safe 
to use it even on non-windowed targets. The ggiWmh* functions just 
fail in that case, where the failure indicates a NOOP.

%package -n %{libname}
Summary:	Main library for libggiwmh
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Main library for libggiwmh.

%package -n %develname
Summary:	Header files for libggiwmh library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d ggiwmh 0

%description -n %develname
Header files for libggiwmh library.

%package -n %staticname
Summary:	Static files for libggiwmh library
Group:		Development/C
Requires:	%develname = %{version}-%{release}
Obsoletes: %mklibname -s -d ggiwmh 0

%description -n %staticname
Static files for libggiwmh library.

%prep
%setup -q
./autogen.sh

%build
export echo=echo

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
export echo=echo

%makeinstall_std

%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/libggiwmh.so.0.0.3
chrpath -d %{buildroot}%{_libdir}/ggi/wmh/display/X_wmh.so
chrpath -d %{buildroot}%{_libdir}/ggi/wmh/display/pseudo_stubs_wmh.so
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING README ChangeLog
%attr(755,root,root)
%config(noreplace) %{_sysconfdir}/ggi/libggiwmh.conf
%attr(755,root,root) %{_libdir}/ggi/wmh/display/*.so
%attr(755,root,root) %{_libdir}/ggi/wmh/display/*.la
%{_mandir}/man3/*

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(644,root,root,755)
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man7/*

%files -n %staticname
%defattr(644,root,root,755)
%{_libdir}/*.a



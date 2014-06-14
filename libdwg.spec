# NOTE: see also http://www.gnu.org/software/libredwg/ (GNU fork under development, no releases yet)
Summary:	LibDWG - free implementation of the DWG file format
Summary(pl.UTF-8):	LibDWG - wolnodostępna implementacja formatu plików DWG
Name:		libdwg
Version:	0.6
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libdwg/%{name}-%{version}.tar.bz2
# Source0-md5:	5801b61de890fd020c3bedfb86870eeb
Patch0:		%{name}-format.patch
URL:		http://libdwg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibDWG is a free C library to read DWG files. DWG is a file format
created in the 70's for the emerging CAD applications. Currently it
is the native file format of AutoCAD, a proprietary CAD program
developed by AutoDesk.

%description -l pl.UTF-8
LibDWG to wolnodostępna biblioteka C do odczytu plików DWG. DWG to
format plików powstały w latach 70. dla powstających aplikacji CAD.
Obecnie jest to natywny format AutoCAD-a - własnościowego programu
CAD rozwijanego przez firmę AutoDesk.

%package devel
Summary:	Header files for LibDWG library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibDWG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LibDWG library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibDWG.

%package static
Summary:	Static LibDWG library
Summary(pl.UTF-8):	Statyczna biblioteka LibDWG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibDWG library.

%description static -l pl.UTF-8
Statyczna biblioteka LibDWG.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdwg.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%lang(eo) %doc LEGUMIN
%attr(755,root,root) %{_bindir}/dwg-dump
%attr(755,root,root) %{_bindir}/dwg-dxf
%attr(755,root,root) %{_bindir}/dwg-preview
%attr(755,root,root) %{_libdir}/libdwg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwg.so.3
%{_mandir}/man1/dwg-dump.1*
%{_mandir}/man1/dwg-dxf.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwg.so
%{_includedir}/dwg.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwg.a

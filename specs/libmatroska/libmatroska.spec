# $Id$

Summary: Multimedia container format library
Name: libmatroska
Version: 0.7.2
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.matroska.org/
Source: http://dl.matroska.org/downloads/libmatroska/libmatroska-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libebml-devel >= 0.7.1

%description
In short, matroska is a new Audio/Video container file format. It is an
advanced and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that allows
infinite extensibility of the format. And full featured because it includes
precise seeking, any audio/video/subtitle codec support including
VCM/ACM/DirectShow compatibility, timecode based format, complex frame
dependencies, chaptering, internationalisation, error protection, tagging,
file attachement, control track (to be defined), menu (to be defined), etc.
All these features are not yet implemented but already defined in the format.


%package devel
Summary: Development files for the Matroska container format library
Group: Development/Libraries
# Static lib, no main package (yet)
#Requires: %{name} = %{version}

%description devel
In short, matroska is a new Audio/Video container file format. It is an
advanced and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that allows
infinite extensibility of the format. And full featured because it includes
precise seeking, any audio/video/subtitle codec support including
VCM/ACM/DirectShow compatibility, timecode based format, complex frame
dependencies, chaptering, internationalisation, error protection, tagging,
file attachement, control track (to be defined), menu (to be defined), etc.
All these features are not yet implemented but already defined in the format.

This package contains the required files to develop programs that will use
the Matroska container format library.


%prep
%setup


%build
# No autotools...
%{__make} -C make/linux %{?_smp_mflags} DEBUGFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} -C make/linux install \
    libdir=%{buildroot}%{_libdir} \
    includedir=%{buildroot}%{_includedir}/matroska


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


# No files for now, as there is only a static library
#files
#defattr(-, root, root, 0755)

%files devel
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.LGPL
%{_includedir}/matroska/
%{_libdir}/*.a


%changelog
* Fri Aug  6 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.

* Tue Aug  3 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Thu Jul  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Initial RPM release.


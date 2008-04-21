# $Id$
# Authority: dries
# Upstream: David Santo Orcero <irbis$orcero,org>

# Screenshot: http://www.orcero.org/irbis/kradview/imagen1.png

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Viewer for DICOM compatible imaging devices
Name: kradview
Version: 1.1.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.orcero.org/irbis/kradview

Source: http://www.orcero.org/irbis/kradview/kradview-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, kdelibs-devel, gettext
%{?fc4:BuildRequires: compat-gcc-32-c++}

%description
kradview is a viewer for images obtained from various sources: X-ray, NMR,
and all DICOM-compatible imaging devices. Its aim is to be a complete
platform for medical imaging and image processing.

%prep
%setup

%build
%{?fc4:export CXX=g++32}
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kradview
%{_bindir}/kradview_client
%{_datadir}/applnk/Utilities/kradview.desktop
%dir %{_datadir}/apps/kradview/
%{_datadir}/apps/kradview/kradviewui.rc
%{_datadir}/doc/HTML/en/kradview/
%{_datadir}/icons/*/*/apps/kradview.png

%changelog
* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Initial package.

# $Id$
# Authority: dries
# Upstream: Dominique Reymond <reymond,d$labogeo,pf>

%define desktop_vendor rpmforge

Summary: Tool for processing and displaying seismic signal data
Name: seismictoolkit
Version: 0.59
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://chez.mana.pf/dominique.reymond/

Source: http://dl.sf.net/seismic-toolkit/stk_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, gtk2-devel, desktop-file-utils

%description
Seismic Toolkit is a tool for processing and displaying seismic signal data 
in a graphical interface. It reads seismic signals in SAC format, and 
provides a number of user operations, such as zooming, filtering, spectral 
analysis, polarisation analysis, time-frequency representation, Hilbert 
transform, and singular value decomposition.

%prep
%setup -n STK_%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Seismic Toolkit
Comment=Process and display seismic signal data
Exec=STK.%{version}
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
autoreconf --force --install --symlink
#automake --add-missing
#(cd Utilities/POLAR_0_05/; automake --add-missing)
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
	--add-category X-Red-Hat-Base               \
	--dir %{buildroot}%{_datadir}/applications  \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/STK.%{version}
%{_datadir}/applications/%{desktop_vendor}-seismictoolkit.desktop

%changelog
* Thu Feb 28 2008 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Mon Feb 11 2008 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sun Jan 13 2008 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Updated to release 0.57.

* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Mon Nov  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Sun Oct 21 2007 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Thu Jun 07 2007 Dries Verachtert <dries@ulyssis.org. - 0.49-1
- Updated to release 0.49.

* Mon Mar 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Updated to release 0.47.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Sat May 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.39-1
- Updated to release 0.39.

* Fri May 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Wed Feb 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.

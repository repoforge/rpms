# $Id$
# Authority: dries
# Upstream: Dominique Reymond <reymond,d$labogeo,pf>

Summary: Tool for processing and displaying seismic signal data
Name: seismictoolkit
Version: 0.38
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://chez.mana.pf/dominique.reymond/

Source: http://chez.mana.pf/dominique.reymond/stk_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/STK.%{version}
%{_datadir}/applications/*seismictoolkit.desktop

%changelog
* Fri May 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Wed Feb 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.

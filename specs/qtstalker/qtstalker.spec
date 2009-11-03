# $Id$
# Authority: dries
# Upstream: Steve Stratos <sstratos$users,sourceforge,net>

Summary: Stock market, commodity and technical analysis charting application
Name: qtstalker
Version: 0.32
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://qtstalker.sourceforge.net/

Source: http://dl.sf.net/qtstalker/qtstalker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++, db4-devel

%description
Stock market, commodity and technical analysis charting app based on the
Qt toolkit. Extendible plugin system for quotes and indicators. Portfolio,
back testing, chart objects and many more features included.

%prep
%setup -n %{name}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Qtstalker
Comment=Stock market charting application
Exec=qtstalker
Encoding=UTF-8
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}
%{__mkdir} rpmdocs
%{__mv} %{buildroot}%{_datadir}/doc/qtstalker/html rpmdocs/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README rpmdocs/html
#%doc %{_mandir}/man?/*
%{_bindir}/qtstalker
%{_libdir}/libqtstalker.so*
%{_libdir}/qtstalker/
%{_datadir}/qtstalker/
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.32-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 24 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Portland (http://portland.freedesktop.org/)

Summary: Freedesktop.org desktop integration tools
Name: xdg-utils
Version: 1.0.2
Release: 1%{?dist}
License: MIT
Group: Applications/System
URL: http://portland.freedesktop.org/wiki/XdgUtils

Source: http://portland.freedesktop.org/download/xdg-utils-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: coreutils, gawk, make
Requires: /bin/sh

Provides: /usr/bin/xdg-desktop-icon
Provides: /usr/bin/xdg-desktop-menu
Provides: /usr/bin/xdg-email
Provides: /usr/bin/xdg-icon-resource
Provides: /usr/bin/xdg-mime
Provides: /usr/bin/xdg-open
Provides: /usr/bin/xdg-screensaver

%description
Xdg-utils is a set of command line tools that assist applications with a
variety of desktop integration tasks. About half of the tools focus on tasks
commonly required during the installation of a desktop application and the
other half focuses on integration with the desktop environment while the
application is running. Even if the desktop components of your application are
limited to an installer, configuration or management tool, Xdg-utils provides
you with an easy way to enhance the usage experience of your customers by
improving the integration of these components in the user's environment. Best
of all, Xdg-utils is provided as open source and free of charge. 

%prep
%setup

%build
%configure

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README RELEASE_NOTES TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 1.0.2-1
- Initial package.

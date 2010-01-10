# $Id$
# Authority: shuff
# Upstream: Portland (http://portland.freedesktop.org/)

Summary:   Freedesktop.org desktop integration tools
Name:      xdg-utils
Version:   1.0.2
Release:   2%{?dist}
License:   MIT
Group:     System Environment/Base
URL:       http://portland.freedesktop.org/wiki/XdgUtils

Source:    http://portland.freedesktop.org/download/xdg-utils-%{version}%{?beta}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Patch1: xdg-utils-1.0-mimeopen.patch
Patch2: xdg-utils-1.0.1-typo.patch
Patch3: xdg-utils-1.0.1-htmlview.patch

BuildRequires: coreutils, gawk, make

Requires: coreutils
Requires: desktop-file-utils
Requires: which

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

%setup -q -n %{name}-%{version}%{?beta}

%patch1 -p1 -b .mimeopen
%patch2 -p1 -b .typo
%patch3 -p1 -b .htmlview

%build

%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README RELEASE_NOTES TODO
%{_bindir}/xdg-*
%{_mandir}/man1/xdg-*

%changelog
* Sun Jan 10 2010 Yury V. Zaytsev <yury@shurup.com> - 1.0.2-2
- Synced the SPEC with CentOS Extras.

* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 1.0.2-1
- Initial package.

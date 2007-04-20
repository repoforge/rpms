# $Id$
# Authority: dries
# Upstream: <vkleinde$yahoo,de>

Summary: GUI for yum
Name: guyum
Version: 0.3.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.guyum.de/

Source: http://dl.sf.net/guyum/guyum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel

%description
GuYum is a GUI for Yum. It has a multi-tabbed search interface. Repositories 
can be enabled/disabled per search request. It is written in C with GTK+.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_sysconfdir}/pam.d/guyum
%{_sysconfdir}/security/console.apps/guyum
%{_bindir}/guyum
%{_sbindir}/guyum
%{_datadir}/guyum/
%{_datadir}/applications/*guyum.desktop

%changelog
* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1
- Initial package.

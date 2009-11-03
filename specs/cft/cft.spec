# $Id$
# Authority: dag

%define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

Summary: Config file tracker
Name: cft
Version: 0.2.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://cft.et.redhat.com/

Source: http://cft.et.redhat.com/download/cft-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby-devel
Requires: ruby, ruby-fam, ruby-rpm >= 1.2.2, puppet >= 0.22.2
Provides: ruby(cft) = %{version}

%description
Cft (pronounced 'sift') follows a sysadmin as she makes changes to the system,
records the changes and produces a puppet manifest from them. Its basic
workings are inspired by Gnome's Sabayon, a tool that watches a user make
configuration changes to their desktop and collects them into a reusable bundle.

Instead of the desktop though, cft is focused on traditional system admins and
how they maintain machines, mostly with command line tools. Cft uses puppet as
its backbone for expressing the configuration of a system, and for understanding
in greater detail what changes the admin has made to the system.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/cft %{buildroot}%{_sbindir}/cft

%{__install} -d -m0755 %{buildroot}%{ruby_sitelibdir}
%{__cp} -av lib/* %{buildroot}%{ruby_sitelibdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%{_sbindir}/cft
%{ruby_sitelibdir}/cft.rb
%{ruby_sitelibdir}/cft/

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)

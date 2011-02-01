# $Id$
# Authority: shuff
# Upstream: Thomas Uehlinger <th.uehlinger$gmx,ch>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/daemons-%{version}

%global rubyabi 1.8

Summary: Daemonize ruby scripts
Name: rubygem-daemons

Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/daemons/

Source: http://rubygems.org/downloads/daemons-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(daemons) = %{version}

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server) to be run as a daemon and to be controlled by simple
start/stop/restart commands. You can also call blocks as daemons and control
them from the parent or just daemonize the current process. Besides this basic
functionality, daemons offers many advanced features like exception backtracing
and logging (in case your ruby script crashes) and monitoring and automatic
restarting of your processes if they crash. 

%prep
%setup -q -c -T

%build
%{__mkdir_p} .%{gemdir}
gem install -V \
	--local \
	--install-dir $(pwd)/%{gemdir} \
	--force --rdoc \
	%{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{gemdir}
%{__cp} -a .%{gemdir}/* %{buildroot}%{gemdir}/


find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%doc %{geminstdir}/Releases
%doc %{geminstdir}/TODO
%doc %{geminstdir}/examples
%doc %{gemdir}/doc/daemons-%{version}
%{gemdir}/cache/daemons-%{version}.gem
%{gemdir}/specifications/daemons-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/lib

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.

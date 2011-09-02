# $Id$
# Authority: shuff
# Upstream: Ryan Davis <technomancy$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/hoe-%{version}

%global rubyabi 1.8

Summary: rake/rubygems helper for Rakefiles
Name: rubygem-hoe

Version: 2.9.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/hoe/

Source: http://rubygems.org/downloads/hoe-%{version}.gem

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(rake) >= 0.8.7
Provides: rubygem(hoe) = %{version}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage and
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, and deployment.

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


%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mv} %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
find %{buildroot}/%{_bindir} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
%{__rm}dir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Hoe.pdf
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{geminstdir}/test
%doc %{gemdir}/doc/hoe-%{version}
%{_bindir}/*
%{gemdir}/cache/hoe-%{version}.gem
%{gemdir}/specifications/hoe-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/template
%exclude %{geminstdir}/.autotest
%exclude %{geminstdir}/.gemtest
%exclude %{geminstdir}/*/.autotest.erb

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 2.9.1-1
- Initial package.

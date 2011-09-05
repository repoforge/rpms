# $Id$
# Authority: shuff
# Upstream: Jim Weirich <jim$weirichhouse.org>

### EL6 ships with rubygem-rake-0.8.7
%{?el6:# Tag: rfx}

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rake-%{version}

%global rubyabi 1.8

Summary: Make-like program for Ruby
Name: rubygem-rake

Version: 0.8.7
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/rake/

Source0: http://rubygems.org/downloads/rake-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(rake) = %{version}

%description
Rake is a Make-like program implemented in Ruby.  Tasks and dependencies are
specified in standard Ruby syntax.

%prep
%setup -c -T

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
%doc %{geminstdir}/CHANGES 
%doc %{geminstdir}/MIT-LICENSE 
%doc %{geminstdir}/README
%doc %{geminstdir}/TODO 
%doc %{geminstdir}/test 
%doc %{geminstdir}/doc
%doc %{gemdir}/doc/rake-%{version}
%{_bindir}/*
%{gemdir}/cache/rake-%{version}.gem
%{gemdir}/specifications/rake-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/install.rb
%{geminstdir}/bin
%{geminstdir}/lib

%changelog
* Tue Jun 28 2011 Yury V. Zaytsev <yury@shurup.com> - 0.8.7-2
- RFX on RHEL6.

* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 0.8.7-1
- Initial package, ported from EPEL package.

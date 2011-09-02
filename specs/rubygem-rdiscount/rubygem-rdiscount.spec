# $Id$
# Authority: shuff
# Upstream: Ryan Tomayko <rtomayko$gmail,com>
# ExcludeDist: el4 el5
# Rationale: rdiscount needs a minimum of Ruby 1.8.6

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rdiscount-%{version}

%global rubyabi 1.8

Summary: Fast C implementation of Markdown for Ruby
Name: rubygem-rdiscount

Version: 1.6.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rtomayko/rdiscount/

Source: http://rubygems.org/downloads/rdiscount-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel >= 1.8.6

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(rdiscount) = %{version}

%description
Discount is an implementation of John Gruber's Markdown markup language in C.
It implements all of the language described in the markdown syntax document and
passes the Markdown 1.0 test suite.

Discount was developed by David Loren Parsons. The Ruby extension is maintained
by Ryan Tomayko.

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
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/BUILDING
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/README.markdown
%doc %{geminstdir}/man
%doc %{geminstdir}/rdiscount.gemspec
%doc %{gemdir}/doc/rdiscount-%{version}
%{_bindir}/*
%{gemdir}/cache/rdiscount-%{version}.gem
%{gemdir}/specifications/rdiscount-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.6.8-1
- Initial package.

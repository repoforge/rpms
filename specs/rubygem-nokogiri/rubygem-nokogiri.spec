# $Id$
# Authority: shuff
# Upstream: Mike Dalessio <mike$csa,net>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/nokogiri-%{version}

%global rubyabi 1.8

Summary: HTML/XML/SAX/Reader parser for Ruby
Name: rubygem-nokogiri

Version: 1.4.4
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://nokogiri.org/

Source: http://rubygems.org/downloads/nokogiri-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(hoe) >= 2.6.2
#BuildRequires: rubygem(minitest) >= 1.6.0
BuildRequires: rubygem(rake-compiler)
#BuildRequires: rubygem(rexical)
#BuildRequires: rubygem(racc)
BuildRequires: rubygem(rubyforge) >= 2.0.4
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(nokogiri) = %{version}

%description
Nokogiri is an HTML, XML, SAX, and Reader parser. Among Nokogiri's many
features is the ability to search documents via XPath or CSS3 selectors. XML is
like violence - if it doesn’t solve your problems, you are not using enough of
it.

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
%doc %{geminstdir}/CHANGELOG.*
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.*
%doc %{geminstdir}/test
%doc %{gemdir}/doc/nokogiri-%{version}
%{_bindir}/*
%{gemdir}/cache/nokogiri-%{version}.gem
%{gemdir}/specifications/nokogiri-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/deps.rip
%{geminstdir}/lib
%{geminstdir}/tasks
%exclude %{geminstdir}/.autotest

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.4.4-1
- Initial package.

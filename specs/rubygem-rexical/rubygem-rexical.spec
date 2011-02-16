# $Id$
# Authority: shuff
# Upstream: Aaron Patterson <aaron.patterson$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rexical-%{version}

%global rubyabi 1.8

Summary: Ruby equivalent of lex/flex
Name: rubygem-rexical

Version: 1.0.5
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/rexical/

Source: http://rubygems.org/downloads/rexical-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(hoe) >= 2.6.2
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(rexical) = %{version}

%description
Rexical is a lexical scanner generator. It is written in Ruby itself, and
generates Ruby program. It is designed for use with Racc.

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
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/DOCUMENTATION.*.rdoc
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.*
%doc %{gemdir}/doc/rexical-%{version}
%{_bindir}/*
%{gemdir}/cache/rexical-%{version}.gem
%{gemdir}/specifications/rexical-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/sample
%{geminstdir}/test

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.0.5-1
- Initial package.

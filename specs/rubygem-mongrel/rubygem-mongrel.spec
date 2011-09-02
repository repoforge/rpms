# $Id$
# Authority: shuff
# Upstream: Zed A. Shaw <zedshaw$zedshaw,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/mongrel-%{version}

%global rubyabi 1.8

Summary: A small fast HTTP library and server in Ruby
Name: rubygem-mongrel

Version: 1.1.5
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/mongrel/

Source: http://rubygems.org/downloads/mongrel-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(cgi_multipart_eof_fix) >= 2.4
Requires: rubygem(daemons) >= 1.0.3
Requires: rubygem(fastthread) >= 1.0.1
Requires: rubygem(gem_plugin) >= 0.2.3

Provides: rubygem(mongrel) = %{version}

%description
A small fast HTTP library and server that runs Rails, Camping, Nitro, and Iowa
apps.

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
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/COPYING 
%doc %{geminstdir}/LICENSE 
%doc %{geminstdir}/README
%doc %{geminstdir}/TODO
%doc %{geminstdir}/examples
%doc %{geminstdir}/ext
%doc %{geminstdir}/test
%doc %{geminstdir}/tools
%doc %{geminstdir}/mongrel-public_cert.pem
%doc %{geminstdir}/mongrel.gemspec
%doc %{gemdir}/doc/mongrel-%{version}
%exclude %{geminstdir}/.require_paths
%exclude %{geminstdir}/Manifest
%{_bindir}/*
%{gemdir}/cache/mongrel-%{version}.gem
%{gemdir}/specifications/mongrel-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/setup.rb
%{geminstdir}/bin
%{geminstdir}/lib

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 1.1.5-1
- Initial package.

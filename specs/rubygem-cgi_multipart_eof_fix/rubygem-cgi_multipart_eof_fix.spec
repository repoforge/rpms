# $Id$
# Authority: shuff
# Upstream: Evan Weaver <evan$cloudbur,st>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/cgi_multipart_eof_fix-%{version}

%global rubyabi 1.8

Summary: Fix an exploitable bug in CGI multipart parsing
Name: rubygem-cgi_multipart_eof_fix

Version: 2.5.0
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/cgi_multipart_eof_fix/

Source: http://rubygems.org/downloads/cgi_multipart_eof_fix-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(cgi_multipart_eof_fix) = %{version}

%description
Fix an exploitable bug in CGI multipart parsing.

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
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/Manifest
%doc %{geminstdir}/README
%doc %{geminstdir}/cgi_multipart_eof_fix.gemspec
%doc %{geminstdir}/test
%doc %{gemdir}/doc/cgi_multipart_eof_fix-%{version}
%{gemdir}/cache/cgi_multipart_eof_fix-%{version}.gem
%{gemdir}/specifications/cgi_multipart_eof_fix-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/lib

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 2.5.0-1
- Initial package.

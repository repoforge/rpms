# $Id$
# Authority: shuff
# Upstream: Michael Jackson <mjijackson$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rack-accept-%{version}

%global rubyabi 1.8

Summary: HTTP Accept header library for Ruby/Rack
Name: rubygem-rack-accept

Version: 0.4.3
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://mjijackson.com/rack-accept/

Source: http://rubygems.org/downloads/rack-accept-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(rack) >= 0.4
Provides: rubygem(rack-accept) = %{version}

%description
Rack::Accept is a suite of tools for Ruby/Rack applications that eases the
complexity of building and interpreting the Accept* family of HTTP request
headers.

Some features of the library are:

* Strict adherence to RFC 2616, specifically section 14
* Full support for the Accept, Accept-Charset, Accept-Encoding, and
  Accept-Language HTTP request headers
* May be used as Rack middleware or standalone
* A comprehensive test suite that covers many edge cases


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
%doc %{geminstdir}/CHANGES
%doc %{geminstdir}/README
%doc %{geminstdir}/rack-accept.gemspec
%doc %{gemdir}/doc/rack-accept-%{version}
%doc %{geminstdir}/doc
%{gemdir}/cache/rack-accept-%{version}.gem
%{gemdir}/specifications/rack-accept-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 0.4.3-1
- Initial package.

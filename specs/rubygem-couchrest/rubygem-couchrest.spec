# $Id$
# Authority: shuff
# Upstream: J. Chris Anderson <jchris$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/couchrest-%{version}

%global rubyabi 1.8

Summary: Interface to CouchDB's RESTful API
Name: rubygem-couchrest

Version: 1.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/couchrest/

Source: http://rubygems.org/downloads/couchrest-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(json) >= 1.4.6
Requires: rubygem(mime-types) >= 1.15
Requires: rubygem(rest-client) >= 1.5.1
Provides: rubygem(couchrest) = %{version}

%description
CouchRest provides a simple interface on top of CouchDB's RESTful HTTP API, as
well as including some utility scripts for managing views and attachments.

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
%doc %{geminstdir}/README.md
%doc %{geminstdir}/THANKS.md
%doc %{geminstdir}/couchrest.gemspec
%doc %{geminstdir}/examples
%doc %{geminstdir}/history.txt
%doc %{gemdir}/doc/couchrest-%{version}
%{gemdir}/cache/couchrest-%{version}.gem
%{gemdir}/specifications/couchrest-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/utils

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.0.1-1
- Initial package.

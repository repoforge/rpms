# $Id$
# Authority: shuff
# Upstream: Jim Weirich <jim$weirichhouse.org>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/builder-%{version}

%global rubyabi 1.8

Summary: Work with structured data in Ruby
Name: rubygem-builder

Version: 3.0.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/builder/

Source: http://rubygems.org/downloads/builder-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(builder) = %{version}

%description
Builder provides a number of builder objects that make creating structured data
simple to do. Currently the following builder objects are supported: 
* XML Markup 
* XML Events 

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
%doc %{geminstdir}/README*
%doc %{geminstdir}/TAGS
%doc %{gemdir}/doc/builder-%{version}
%doc %{geminstdir}/doc
%{gemdir}/cache/builder-%{version}.gem
%{gemdir}/specifications/builder-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 3.0.0-1
- Initial package.

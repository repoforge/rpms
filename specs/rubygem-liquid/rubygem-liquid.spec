# $Id$
# Authority: shuff
# Upstream: Tobias Luetke <tobi$leetsoft,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/liquid-%{version}

%global rubyabi 1.8

Summary: Secure, non-evaling end user template engine for Ruby
Name: rubygem-liquid

Version: 2.2.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.liquidmarkup.org/

Source: http://rubygems.org/downloads/liquid-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(liquid) = %{version}

%description
Liquid is an extraction from the e-commerce system Shopify. Shopify powers many
thousands of e-commerce stores which all call for unique designs. For this we
developed Liquid which allows our customers complete design freedom while
maintaining the integrity of our servers.

Liquid has been in production use since June 2006 and is now used by many other
hosted web applications.

It was developed to for usage in Ruby on Rails web applications and integrates
seamlessly as a plugin but it also works excellently as a stand alone library. 

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


find %{buildroot}%{geminstdir}/lib -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/lib -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.md
%doc %{gemdir}/doc/liquid-%{version}
%{gemdir}/cache/liquid-%{version}.gem
%{gemdir}/specifications/liquid-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/lib

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 2.2.2-1
- Initial package.

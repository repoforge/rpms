# $Id$
# Authority: shuff
# Upstream: Maik Schmidt <contact$maik-schmidt,de>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/xml-simple-%{version}

%global rubyabi 1.8

Summary: Ruby port of Perl XML::Simple
Name: rubygem-xml-simple

Version: 1.0.14
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://xml-simple.rubyforge.org/

Source: http://rubygems.org/downloads/xml-simple-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(xml-simple) = %{version}

%description
Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple. 


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
%doc %{gemdir}/doc/xml-simple-%{version}
%{gemdir}/cache/xml-simple-%{version}.gem
%{gemdir}/specifications/xml-simple-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/lib

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 1.0.14-1
- Initial package.

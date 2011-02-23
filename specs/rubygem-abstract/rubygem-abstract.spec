# $Id$
# Authority: shuff
# Upstream: Makoto Kuwata <kwa$kuwata-lab,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/abstract-%{version}

%global rubyabi 1.8

Summary: Define abstract methods in Ruby
Name: rubygem-abstract

Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/abstract/

Source: http://rubygems.org/downloads/abstract-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(abstract) = %{version}

%description
'abstract.rb' is a library which enable you to define abstract methods in Ruby.

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
%doc %{geminstdir}/ChangeLog
%doc %{geminstdir}/README.txt
%doc %{geminstdir}/abstract.gemspec
%doc %{gemdir}/doc/abstract-%{version}
%{gemdir}/cache/abstract-%{version}.gem
%{gemdir}/specifications/abstract-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/setup.rb
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.0.0-1
- Initial package.

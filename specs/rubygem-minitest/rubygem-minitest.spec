# $Id$
# Authority: shuff
# Upstream: Ryan Davis <technomancy$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/minitest-%{version}

%global rubyabi 1.8

Summary: Unit testing framework for Ruby
Name: rubygem-minitest

Version: 2.0.2
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/minitest/

Source: http://rubygems.org/downloads/minitest-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(hoe) >= 2.8.0
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(minitest) = %{version}

%description
minitest provides a complete suite of testing facilities supporting TDD, BDD,
mocking, and benchmarking. minitest/unit is a small and incredibly fast unit
testing framework. It provides a rich set of assertions to make your tests
clean and readable. minitest/spec is a functionally complete spec engine. It
hooks onto minitest/unit and seamlessly bridges test assertions over to spec
expectations. minitest/benchmark is an awesome way to assert the performance of
your algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential one!
minitest/mock by Steven Baker, is a beautifully tiny mock object framework.
minitest/pride shows pride in testing and adds coloring to your test output.
minitest/unit is meant to have a clean implementation for language implementors
that need a minimal set of methods to bootstrap a working test suite. For
example, there is no magic involved for test-case discovery.

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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{geminstdir}/test
%doc %{gemdir}/doc/minitest-%{version}
%{gemdir}/cache/minitest-%{version}.gem
%{gemdir}/specifications/minitest-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/design_rationale.rb
%{geminstdir}/lib
%exclude %{geminstdir}/.autotest

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 2.0.2-1
- Initial package.

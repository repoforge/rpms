# $Id$
# Authority: shuff
# Upstream: smtlaissezfaire <scott$railsnewbie,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/markaby-%{version}

%global rubyabi 1.8

Summary: HTML templating system for Ruby
Name: rubygem-markaby

Version: 0.7.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://markaby.github.com/markaby/

Source: http://rubygems.org/downloads/markaby-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(builder) >= 2.0.0

Provides: rubygem(markaby) = %{version}
Provides: rubygem(Markaby) = %{version}

%description
Markaby is a very short bit of code for writing HTML pages in pure Ruby. It is
an alternative to ERB which weaves the two languages together. Also a
replacement for templating languages which use primitive languages that blend
with HTML. 

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
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/VERSION
%doc %{geminstdir}/Markaby.gemspec
%doc %{gemdir}/doc/markaby-%{version}
%{gemdir}/cache/markaby-%{version}.gem
%{gemdir}/specifications/markaby-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/garlic.rb
%{geminstdir}/init.rb
%exclude %{geminstdir}/.gitignore

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 0.7.1-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Alexis Sellier <alexis$cloudhead,net>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/mutter-%{version}

%global rubyabi 1.8

Summary: Tiny command-line interface library with lots of style
Name: rubygem-mutter

Version: 0.5.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/mutter/

Source: http://rubygems.org/downloads/mutter-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(mutter) = %{version}

%description
    $ my words come out, 
        in color and
            style

mutter takes the concepts of separation of style & content to the command-line!


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
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%doc %{geminstdir}/VERSION
%doc %{geminstdir}/mutter.gemspec
%doc %{gemdir}/doc/mutter-%{version}
%{gemdir}/cache/mutter-%{version}.gem
%{gemdir}/specifications/mutter-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/spec
%exclude %{geminstdir}/.document
%exclude %{geminstdir}/.gitignore

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 0.5.3-1
- Initial package.

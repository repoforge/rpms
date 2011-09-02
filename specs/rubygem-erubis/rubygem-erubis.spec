# $Id$
# Authority: shuff
# Upstream: Makoto Kuwata <kwa$kuwata-lab,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/erubis-%{version}

%global rubyabi 1.8

Summary: Implementation of eRuby
Name: rubygem-erubis

Version: 2.6.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.kuwata-lab.com/erubis/

Source: http://rubygems.org/downloads/erubis-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(abstract) >= 1.0.0

Provides: rubygem(erubis) = %{version}

%description
Erubis is a fast, secure, and very extensible implementation of eRuby. It has
the following features.

* Very fast, almost three times faster than ERB and about ten percent faster
  than eruby (implemented in C).
* File caching of converted Ruby script support.
* Auto escaping (sanitizing) support, it means that '<%= %>' can be escaped in
  default. It is desirable for web application.
* Spaces around '<% %>' are trimmed automatically only when '<%' is at the
  beginning of line and '%>' is at the end of line.
* Embedded pattern changeable (default '<% %>'), for example '[% %]' or '<? ?>'
  are available.
* Enable to handle Processing Instructions (PI) as embedded pattern (ex. '<?rb
  ... ?>'). This is desirable for XML/HTML than '<% .. %>' because the latter
  breaks HTML design but the former doesn't.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript).
* Context object available and easy to combine eRuby template with YAML
  datafile.
* Print statement available.
* Easy to expand and customize in subclass.
* Ruby on Rails support.
* Mod_ruby support.


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


%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mv} %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
find %{buildroot}/%{_bindir} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
%{__rm}dir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGES.txt
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/README.txt
%doc %{geminstdir}/benchmark
%doc %{geminstdir}/contrib
%doc %{geminstdir}/doc-api
%doc %{geminstdir}/examples
%doc %{gemdir}/doc/erubis-%{version}
%doc %{geminstdir}/doc
%{_bindir}/*
%{gemdir}/cache/erubis-%{version}.gem
%{gemdir}/specifications/erubis-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/setup.rb
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 2.6.6-1
- Initial package.

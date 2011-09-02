# $Id$
# Authority: shuff
# Upstream: Blake Mizerany <blake.mizerany$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/sinatra-%{version}

%{?el6:%define _has_ruby_186 1}

%global rubyabi 1.8

Summary: Classy web-development dressed in a DSL
Name: rubygem-sinatra

Version: 1.1.3
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://sinatrarb.com/

Source: http://rubygems.org/downloads/sinatra-%{version}.gem

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: rdoc
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(builder)
#Requires: rubygem(coffee-script)
Requires: rubygem(erubis)
Requires: rubygem(less)
Requires: rubygem(liquid)
Requires: rubygem(markaby)
Requires: rubygem(nokogiri)
Requires: rubygem(rack) < 2.0
Requires: rubygem(radius)
%{?_has_ruby_186:Requires: rubygem(rdiscount)}
Requires: rubygem(RedCloth)
#Requires: rubygem(therubyracer)
Requires: rubygem(tilt) >= 1.2.2
Requires: rubygem(tilt) < 2.0
Provides: rubygem(sinatra) = %{version}

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort:

    # myapp.rb
    require 'sinatra'

    get '/' do
      'Hello world!'
    end

Note: this Sinatra package does not include support for CoffeeScript templates.

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
%doc %{geminstdir}/AUTHORS
%doc %{geminstdir}/CHANGES
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README*
%doc %{geminstdir}/sinatra.gemspec
%doc %{gemdir}/doc/sinatra-%{version}
%{gemdir}/cache/sinatra-%{version}.gem
%{gemdir}/specifications/sinatra-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 1.1.3-1
- Initial package.

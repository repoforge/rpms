# $Id$
# Authority: shuff
# Upstream: Glenn Rempe <glenn$rempe,us>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/amazon-ec2-%{version}

%global rubyabi 1.8

Summary: Ruby library for Amazon EC2 and other services
Name: rubygem-amazon-ec2

Version: 0.9.17
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/amazon-ec2/

Source: http://rubygems.org/downloads/amazon-ec2-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(xml-simple) >= 1.0.12
Provides: rubygem(amazon-ec2) = %{version}

%description
Amazon Web Services offers a compute power on demand capability known as the
Elastic Compute Cloud (EC2). The server resources in the cloud can be
provisioned on demand by making HTTP Query API calls to EC2.

This ‘amazon-ec2’ Ruby Gem is an interface library that can be used to interact
with the Amazon EC2 system and control server resources on demand from your
Ruby scripts, or from applications written in your Ruby framework of choice
(Ruby on Rails, Merb, etc.).

More recently, support has been added for the following EC2 related AWS API’s
as well:

* Autoscaling
* Cloudwatch
* Elastic Load Balancing (ELB)
* Relational Database Service (RDS)


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
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/ChangeLog
%doc %{geminstdir}/Gemfile*
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/VERSION
%doc %{geminstdir}/amazon-ec2.gemspec
%doc %{geminstdir}/deps.rip
%doc %{gemdir}/doc/amazon-ec2-%{version}
%{_bindir}/*
%{gemdir}/cache/amazon-ec2-%{version}.gem
%{gemdir}/specifications/amazon-ec2-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test
%{geminstdir}/wsdl
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.yardopts

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 0.9.17-1
- Initial package.

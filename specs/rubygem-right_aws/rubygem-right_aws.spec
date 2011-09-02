# $Id$
# Authority: shuff
# Upstream: RightScale, Inc. <rubygems$rightscale,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/right_aws-%{version}

%global rubyabi 1.8

Summary: RightScale Ruby interface to AWS
Name: rubygem-right_aws

Version: 2.0.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rightscale.rubyforge.org/

Source: http://rubygems.org/downloads/right_aws-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(right_http_connection) >= 1.2.1

Provides: rubygem(right_aws) = %{version}

%description
The RightScale AWS gems have been designed to provide a robust, fast, and
secure interface to Amazon EC2, EBS, S3, SQS, SDB, and CloudFront. These gems
have been used in production by RightScale since late 2006 and are being
maintained to track enhancements made by Amazon. The RightScale AWS gems
comprise:

* RightAws::Ec2 — interface to Amazon EC2 (Elastic Compute Cloud), VPC (Virtual
  Private Cloud) and the associated EBS (Elastic Block Store)
* RightAws::S3 and RightAws::S3Interface — interface to Amazon S3 (Simple
  Storage Service)
* RightAws::Sqs and RightAws::SqsInterface — interface to first-generation
  Amazon SQS (Simple Queue Service)
* RightAws::SqsGen2 and RightAws::SqsGen2Interface — interface to
  second-generation Amazon SQS (Simple Queue Service)
* RightAws::SdbInterface and RightAws::ActiveSdb — interface to Amazon SDB
  (SimpleDB)
* RightAws::AcfInterface — interface to Amazon CloudFront, a content
  distribution service
* RightAws::AsInterface — interface to Amazon Auto Scaling
* RightAws::AcwInterface — interface to Amazon Cloud Watch
* RightAws::ElbInterface — interface to Amazon Elastic Load Balancer
* RightAws::RdsInterface — interface to Amazon RDS instances


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
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{gemdir}/doc/right_aws-%{version}
%{gemdir}/cache/right_aws-%{version}.gem
%{gemdir}/specifications/right_aws-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 2.0.0-1
- Initial package.

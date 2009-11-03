# $Id$
# Authority: shuff
# Upstream: Léon Brocard <leon$astray,com>

## Still needs MooseX::StrictConstructor, MooseX::Types::DateTime
## Test

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Amazon-S3

Summary: Use the Amazon S3 - Simple Storage Service
Name: perl-%{real_name}
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Amazon-S3/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/Net-Amazon-S3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP) >= 0.88
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Data::Stream::Bulk) >= 0.06
BuildRequires: perl(DateTime::Format::HTTP)
BuildRequires: perl(DateTime::Format::ISO8601)
BuildRequires: perl(Digest::HMAC_SHA1)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::MD5::File)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::stat)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::File) >= 1.14
BuildRequires: perl(LWP::UserAgent::Determined)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Moose) >= 0.85
BuildRequires: perl(MooseX::StrictConstructor) >= 0.08
BuildRequires: perl(MooseX::Types::DateTimeX)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More) >= 0.01
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::LibXML::XPathContext)
BuildRequires: perl(URI::Escape)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Class::MOP) >= 0.88
Requires: perl(Class::Accessor::Fast)
Requires: perl(Data::Stream::Bulk) >= 0.06
Requires: perl(DataTime::Format::HTTP)
Requires: perl(DataTime::Format::ISO8601)
Requires: perl(Digest::HMAC_SHA1)
Requires: perl(Digest::MD5)
Requires: perl(Digest::MD5::File)
Requires: perl(File::stat)
Requires: perl(HTTP::Date)
Requires: perl(HTTP::Status)
Requires: perl(IO::File) >= 1.14
Requires: perl(LWP::UserAgent::Determined)
Requires: perl(MIME::Base64)
Requires: perl(Moose) >= 0.85
Requires: perl(MooseX::StrictConstructor) >= 0.08
Requires: perl(MooseX::Types::DateTimeX)
Requires: perl(Regexp::Common)
Requires: perl(XML::LibXML)
Requires: perl(XML::LibXML::XPathContext)
Requires: perl(URI::Escape)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a Perlish interface to Amazon S3. From the developer
blurb: "Amazon S3 is storage for the Internet. It is designed to make web-scale
computing easier for developers. Amazon S3 provides a simple web services
interface that can be used to store and retrieve any amount of data, at any
time, from anywhere on the web. It gives any developer access to the same
highly scalable, reliable, fast, inexpensive data storage infrastructure that
Amazon uses to run its own global network of web sites. The service aims to
maximize benefits of scale and to pass those benefits on to developers".

To find out more about S3, please visit: http://s3.amazonaws.com/

To use this module you will need to sign up to Amazon Web Services and provide
an "Access Key ID" and " Secret Access Key". If you use this module, you will
incurr costs as specified by Amazon. Please check the costs. If you use this
module with your Access Key ID and Secret Access Key you must be responsible
for these costs.


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net
%{perl_vendorlib}/*
%{_bindir}/*

%changelog
* Thu Oct 29 2009 Steve Huff <shuff@vecna.org> - 0.52-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Alexis Sukrieh <sukria$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Dancer

Summary: A minimal-effort oriented web application framework
Name: perl-Dancer
Version: 1.3072
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://perldancer.org/

Source: http://www.cpan.org/modules/by-module/Dancer/Dancer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.5
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Body) >= 1.07
BuildRequires: perl(HTTP::Server::Simple::PSGI) >= 0.11
BuildRequires: perl(LWP)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.5
Requires: perl(Carp)
Requires: perl(Clone)
Requires: perl(Data::Dumper)
Requires: perl(Encode)
Requires: perl(FindBin)
Requires: perl(File::Basename)
Requires: perl(File::Spec)
Requires: perl(Getopt::Long)
Requires: perl(HTTP::Body) >= 1.07
Requires: perl(HTTP::Server::Simple::PSGI) >= 0.11
Requires: perl(JSON)
Requires: perl(LWP)
Requires: perl(MIME::Types)
Requires: perl(Template)
Requires: perl(Time::HiRes)
Requires: perl(URI)
Requires: perl(XML::Simple)
Requires: perl(YAML)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Dancer is a web application framework designed to be as effortless as possible
for the developer, taking care of the boring bits as easily as possible, yet
staying out of your way and letting you get on with writing your code.

Dancer aims to provide the simplest way for writing web applications, and
offers the flexibility to scale between a very simple lightweight web service
consisting of a few lines of code in a single file, all the way up to a more
complex fully-fledged web application with session support, templates for views
and layouts, etc.

If you don't want to write CGI scripts by hand, and find Catalyst too big or
cumbersome for your project, Dancer is what you need.

Dancer has few pre-requisites, so your Dancer webapps will be easy to deploy.

Dancer apps can be used with a an embedded web server (great for easy testing),
and can run under PSGI/Plack for easy deployment in a variety of webserver
environments.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES LICENSE META.yml README TODO
%doc examples/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/Dancer.pm
%{perl_vendorlib}/Dancer/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Thu Aug 25 2011 Steve Huff <shuff@vecna.org> - 1.3072-1
- Update to version 1.3072.

* Wed Jun 15 2011 Steve Huff <shuff@vecna.org> - 1.3060-1
- Update to version 1.3060.

* Thu May 05 2011 Steve Huff <shuff@vecna.org> - 1.3040-1
- Initial package.

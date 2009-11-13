# $Id$
# Authority: shuff
# Upstream: Michael Frankl <mfrankl$seibert-media,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-HTMLDoc

Summary: Perl interface to the htmldoc program for producing PDF-Files from HTML-Content
Name: perl-%{real_name}
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-HTMLDoc/

Source: http://search.cpan.org/CPAN/authors/id/M/MF/MFRANKL/HTML-HTMLDoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: htmldoc
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: htmldoc
Requires: perl
Requires: perl(IPC::Open3)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This Module provides an OO-interface to the htmldoc programm. To install this
module you have to install the htmldoc program first. You can get it from
http://www.htmldoc.org .

You can use it to produce PDF or PS files from a HTML-document. Currently many
but not all parameters of HTMLDoc are supported.

You need to have HTMLDoc installed before installing this module.

All the pdf-Methods return true for success or false for failure. You can test
if errors occurred by calling the error-method.

Normaly this module uses IPC::Open3 for communacation with the HTMLDOC process.
However, in mod_perl-environments there appear problems with this module
because the standard-output can not be captured. For this problem this module
provides a fix doing the communication in file-mode.

For this you can specify the parameter mode in the constructor: my $htmldoc =
new HTMLDoc('mode'=>'file', 'tmpdir'=>'/tmp');

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/*

%changelog
* Fri Nov 13 2009 Steve Huff <shuff@vecna.org> - 0.10-1
- Initial package.

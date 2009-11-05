# $Id$
# Authority: shuff
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Captcha-reCAPTCHA

Summary: A Perl implementation of the reCAPTCHA API
Name: perl-%{real_name}
Version: 0.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Captcha-reCAPTCHA/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDYA/Captcha-reCAPTCHA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(ExtUtils::MakeMaker::Coverage) # not yet packaged
BuildRequires: perl(HTML::Tiny) >= 0.904
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(HTML::Tiny) >= 0.904
Requires: perl(LWP::UserAgent)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
reCAPTCHA is a hybrid mechanical turk and captcha that allows visitors who
complete the captcha to assist in the digitization of books.

From http://recaptcha.net/learnmore.html:

    reCAPTCHA improves the process of digitizing books by sending words that
    cannot be read by computers to the Web in the form of CAPTCHAs for
    humans to decipher. More specifically, each word that cannot be read
    correctly by OCR is placed on an image and used as a CAPTCHA. This is
    possible because most OCR programs alert you when a word cannot be read
    correctly.

This Perl implementation is modelled on the PHP interface that can be found
here:

    http://recaptcha.net/plugins/php/

To use reCAPTCHA you need to register your site here:

    https://admin.recaptcha.net/recaptcha/createsite/

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
%doc Changes MANIFEST META.yml README SIGNATURE examples/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Captcha/
%{perl_vendorlib}/Captcha/*

%changelog
* Thu Nov 05 2009 Steve Huff <shuff@vecna.org> - 0.92-1
- Initial package.

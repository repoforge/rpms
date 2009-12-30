# $Id$
# Authority: shuff
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Sender

Summary: A library for sending email
Name: perl-Email-Sender
Version: 0.093380
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Sender/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Sender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Email::Abstract) >= 3
BuildRequires: perl(Email::Address)
BuildRequires: perl(Email::Simple) >= 1.998
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose) >= 0.70
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sys::Hostname::Long)
Requires: perl(Capture::Tiny)
Requires: perl(Carp)
Requires: perl(Cwd)
Requires: perl(Email::Abstract) >= 3
Requires: perl(Email::Address)
Requires: perl(Email::Simple) >= 1.998
Requires: perl(Fcntl)
Requires: perl(File::Basename)
Requires: perl(File::Find)
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(FindBin)
Requires: perl(List::MoreUtils)
Requires: perl(Moose) >= 0.70
Requires: perl(Net::SMTP)
Requires: perl(Scalar::Util)
Requires: perl(Sys::Hostname::Long)

%filter_from_requires /^perl*/d
%filter_setup

%description
Perl module for sending mail.

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

### Clean up docs
find xt/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.json README xt/
%doc %{_mandir}/man3/Email::Sender.3pm*
%doc %{_mandir}/man3/Email::Sender::*.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Sender/
%{perl_vendorlib}/Email/Sender.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.093380-1
- Updated to version 0.093380.

* Wed Sep 16 2009 Steve Huff <shuff@vecna.org> - 0.091941-1
- Initial package.
- Doesn't build; depends on perl(Capture::Tiny), which we don't yet have.

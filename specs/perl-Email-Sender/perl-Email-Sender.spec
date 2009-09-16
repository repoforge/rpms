# $Id$
# Authority: shuff
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Sender

Summary: A library for sending email
Name: perl-Email-Send
Version: 0.091940
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Sender/

Source: http://www.cpan.org/modules/by-module/Email/Email-Sender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Capture::Tiny) >= 0
BuildRequires: perl(Carp) >= 0
BuildRequires: perl(Cwd) >= 0
BuildRequires: perl(Email::Abstract) >= 3
BuildRequires: perl(Email::Address) >= 0
BuildRequires: perl(Email::Simple) >= 1.998
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename) >= 0
BuildRequires: perl(File::Find) >= 0
BuildRequires: perl(File::Spec) >= 0
BuildRequires: perl(File::Temp) >= 0
BuildRequires: perl(FindBin) >= 0
BuildRequires: perl(Fcntl) >= 0
BuildRequires: perl(List::MoreUtils) >= 0
BuildRequires: perl(Moose) >= 0
BuildRequires: perl(Net::SMTP) >= 0
BuildRequires: perl(Scalar::Util) >= 0
BuildRequires: perl(Sys::Hostname::Long) >= 0
BuildRequires: perl(Test::More) >= 0.47
Requires: perl
Requires: perl(Capture::Tiny) >= 0
Requires: perl(Carp) >= 0
Requires: perl(Cwd) >= 0
Requires: perl(Email::Abstract) >= 3
Requires: perl(Email::Address) >= 0
Requires: perl(Email::Simple) >= 1.998
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(File::Basename) >= 0
Requires: perl(File::Find) >= 0
Requires: perl(File::Spec) >= 0
Requires: perl(File::Temp) >= 0
Requires: perl(FindBin) >= 0
Requires: perl(Fcntl) >= 0
Requires: perl(List::MoreUtils) >= 0
Requires: perl(Moose) >= 0
Requires: perl(Net::SMTP) >= 0
Requires: perl(Scalar::Util) >= 0
Requires: perl(Sys::Hostname::Long) >= 0
Requires: perl(Test::More) >= 0.47
AutoReq: no

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
* Wed Sep 16 2009 Steve Huff <shuff@vecna.org> - 0.091941-1
- Initial package.
- Doesn't build; depends on perl(Capture::Tiny), which we don't yet have.

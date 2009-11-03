# $Id$
# Authority: dag
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Transport-Dbx

Summary: Perl module to parse Outlook Express mailboxes
Name: perl-Mail-Transport-Dbx
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Transport-Dbx/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Transport-Dbx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Mail-Transport-Dbx is a Perl module to parse Outlook Express mailboxes.

This package contains the following Perl module:

    Mail::Transport::Dbx

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/Mail::Transport::Dbx.3pm*
%dir %{perl_vendorarch}/Mail/
%dir %{perl_vendorarch}/Mail/Transport/
%{perl_vendorarch}/Mail/Transport/Dbx.pm
%dir %{perl_vendorarch}/auto/Mail/
%dir %{perl_vendorarch}/auto/Mail/Transport/
%{perl_vendorarch}/auto/Mail/Transport/Dbx/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)

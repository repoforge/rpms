# $Id$
# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Reply

Summary: Reply to mails
Name: perl-Email-Reply
Version: 1.200
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Reply/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Reply-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl package to reply to mails.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Email::Reply*
%{perl_vendorlib}/Email/Reply.pm

%changelog
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.200-1
- Initial package.

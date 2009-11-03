# $Id$
# Authority: shuff
# Upstream: Alexandr Ciornii <alexchorny$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Ping-External

Summary: Cross-platform interface to ICMP "ping" utilities
Name: perl-Net-Ping-External
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Ping-External/

Source: http://www.cpan.org/modules/by-module/Net/Net-Ping-External-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Net::Ping::External is a module which interfaces with the "ping" command
on many systems. It presently provides a single function, ping(), that
takes in a hostname and (optionally) a timeout and returns true if the
host is alive, and false otherwise. Unless you have the ability (and
willingness) to run your scripts as the superuser on your system, this
module will probably provide more accurate results than Net::Ping will.

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
%doc %{_mandir}/man3/Net::Ping::External.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Ping/
%{perl_vendorlib}/Net/Ping/External.pm

%changelog
* Fri Sep 18 2009 Steve Huff <shuff@vecna.org> - 0.13-1
- Initial package.

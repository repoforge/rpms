# $Id$
# Authority: dries
# Upstream: Jay Rogers <jay$rgrs,com>

### EL6 ships with perl-Net-Telnet-3.03-11.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Net-Telnet-3.03-5
%{?el5:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Telnet

Summary: Interface to telnet
Name: perl-Net-Telnet
Version: 3.03
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Telnet/

Source: http://www.cpan.org/modules/by-module/Net/Net-Telnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Net::Telnet allows you to make client connections to a TCP port
and do network I/O, especially to a port using the TELNET
protocol.  Simple I/O methods such as print, get, and getline are
provided.  More sophisticated interactive features are provided
because connecting to a TELNET port ultimately means communicating
with a program designed for human interaction.  These interactive
features include the ability to specify a timeout and to wait for
patterns to appear in the input stream, such as the prompt from a
shell.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_mandir}/man3/Net::Telnet.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Telnet.pm

%changelog
* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 3.03-2
- RFX'ed on RHEL6.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 3.03-1
- Initial package.

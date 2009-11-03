# $Id$
# Authority: dag
# Upstream: Derrick Daugherty <rfc$dewn,com>

Summary: Utility for searching and alternatively displaying RFC's
Name: rfc
Version: 3.21
Release: 1.2%{?dist}
License: distributable
Group: Applications/Internet
URL: http://www.dewn.com/rfc/

Source: http://www.dewn.com/rfc/rfc-%{version}
Source1: http://www.dewn.com/rfc/changelog
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Obsoletes: rfcutil <= %{version}-%{release}
BuildRequires: links
Requires: perl, links

%description
rfc-util allows you to specify a number of an RFC, or a string
that you're looking for, and return all related RFC's. You can also
throw in the -l switch and have it spawn lynx to view the RFC.

%prep
%setup -c -T
%{__cp} -apv %{SOURCE0} ./rfc
%{__cp} -apv %{SOURCE1} ./changelog

%{__perl} -pi.orig -e '
		s|\$viewer -dump|links -source|;
		s|^(my \@VIEWER)=qw\(w3m lynx\);$|$1=qw(\$TEXTBROWSER links lynx w3m \$BROWSER);|;
		s|/ftp.isi.edu/in-notes/iana|/www.iana.org|;
		s|^(\$indexpath)=.+$|$1="%{_localstatedir}/lib/rfc/rfc-index";|;
		s|^(\$servpath)=.+$|$1="%{_localstatedir}/lib/rfc/nmap-services";|;
	' rfc

%{__perl} -pi-rpm -e '
		s|^(\$indexpath)=.+$|$1="%{buildroot}%{_localstatedir}/lib/rfc/rfc-index";|;
		s|^(\$servpath)=.+$|$1="%{buildroot}%{_localstatedir}/lib/rfc/nmap-services";|;
	' rfc

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rfc-rpm %{buildroot}%{_bindir}/rfc
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/rfc/
%{__perl} ./rfc -i
%{__perl} ./rfc -n -i

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog
%{_bindir}/rfc

%defattr(0644, root, root, 0755)
%verify(not md5 mtime size) %{_localstatedir}/lib/rfc/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.21-1.2
- Rebuild for Fedora Core 5.

* Sat Jul 31 2004 Dag Wieers <dag@wieers.com> - 3.21-1
- Initial package. (using DAR)

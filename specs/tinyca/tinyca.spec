# Authority: dag

Summary: A Graphical Tool for Managing a Certification Authority.
Name: tinyca
Version: 0.5.4
Release: 0
License: GPL
Group: Applications/Internet
URL: http://tinyca.sm-zone.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://tinyca.sm-zone.net/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: openssl, Gtk-Perl

%description 
TinyCA is a graphical tool written in Perl/Gtk to manage a small
Certification Authority (CA) using openssl.

TinyCA supports - creation and revocation of x509 - S/MIME
certificates.

%prep
%setup -n TinyCA

%build
%{__perl} -pi.orig -e '
		s|./lib|%{_datadir}/tinyca|g;
		s|./locale|%{_datadir}/locale|g;
		s|./templates|%{_sysconfdir}/tinyca|g;
	' tinyca
%{__make} -C po

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/tinyca/ \
			%{buildroot}%{_sysconfdir}/tinyca/ \
			%{buildroot}%{_datadir}/locale/de/LC_MESSAGES/
%{__install} -m0644 lib/*.pm %{buildroot}%{_datadir}/tinyca/
%{__install} -m0644 templates/openssl.cnf %{buildroot}%{_sysconfdir}/tinyca/
%{__install} -m0755 tinyca %{buildroot}%{_bindir}
%{__install} -m0644 locale/de/LC_MESSAGES/tinyca.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGES
%config %{_sysconfdir}/tinyca/
%{_bindir}/*
%{_datadir}/tinyca/

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)

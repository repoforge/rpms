# $Id$
# Authority: dag
# Upstream: <sm@sm-zone.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define real_name TinyCA

Summary: Graphical Tool for Managing a Certification Authority
Name: tinyca
Version: 0.6.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tinyca.sm-zone.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://tinyca.sm-zone.net/tinyca-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: openssl, Gtk-Perl

%description 
TinyCA is a graphical tool written in Perl/Gtk to manage a small
Certification Authority (CA) using openssl.

TinyCA supports - creation and revocation of x509 - S/MIME
certificates.

%prep
%setup -n %{real_name}

%{__perl} -pi.orig -e '
		s|./lib|%{_datadir}/tinyca|g;
		s|./locale|%{_datadir}/locale|g;
		s|./templates|%{_sysconfdir}/tinyca|g;
	' tinyca

%{__cat} <<EOF >tinyca.desktop
[Desktop Entry]
Name=TinyCA Certification Authority
Comment=Work with various certificates
Exec=tinyca
Type=Application
Encoding=UTF-8
Icon=redhat-accessories.png
Categories=GNOME;Application;Utility;
EOF

%build
%{__make} -C po

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 templates/openssl.cnf %{buildroot}%{_sysconfdir}/tinyca/openssl.cnf
%{__install} -D -m0755 tinyca %{buildroot}%{_bindir}/tinyca
%{__install} -D -m0644 locale/de/LC_MESSAGES/tinyca.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/tinyca.mo

%{__install} -d -m0755 %{buildroot}%{_datadir}/tinyca/
%{__install} -m0644 lib/*.pm %{buildroot}%{_datadir}/tinyca/

%find_lang %{name}

%if %{dfi}
	%{__install} -D -m0644 tinyca.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/tinyca.desktop
%else   
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		tinyca.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGES
%config %{_sysconfdir}/tinyca/
%{_bindir}/*
%{_datadir}/tinyca/
%if %{dfi}
        %{_datadir}/gnome/apps/Utilities/*.desktop
%else   
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Initial package. (using DAR)

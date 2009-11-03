# $Id$
# Authority: dag

# SourceDists: rh7

%define aversion %(rpm -q apache-devel --qf '%{RPMTAG_VERSION}' | tail -1)
%define real_version 1.3.26.1a

Summary: Gzip compression module for apache
Name: mod_gzip
Version: 1.3.26
Release: 0.1a.2%{?dist}
License: Apache License
Group: System Environment/Daemons
URL: http://www.schroepl.net/projekte/mod_gzip/

Source: http://dl.sf.net/mod-gzip/mod_gzip-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, apache-devel
Requires: apache = %{aversion}, mm >= 1.0

%description
mod_gzip is an Internet Content Acceleration module for the popular Apache
Web Server.

If standard IETF Content Encoding is what you need to accelerate your Apache
Web Server, reduce your CPU load, and deliver 75-80 percent less data with
no loss of content to your users at all times then look no farther. HSC's
mod_gzip is all that you need.

mod_gzip uses the well established and publicly available IETF ( Internet
Engineering Task Force ) Content-Encoding standards in conjunction with
publicy available GZIP compression libraries such as ZLIB ( Copyright ©
1995-1998 Jean-loup Gailly and Mark Adler ) to deliver dynamically
compressed content 'on the fly' to any browser or user-agent that is capable
of receiving it. It is a software based solution that runs perfectly in
conjunction with any Apache Web Server on both UNIX and Win32 platforms.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<'EOF' >mod_gzip.conf
<IfModule mod_gzip.c>
	mod_gzip_on                 yes
	mod_gzip_dechunk            yes
	mod_gzip_send_vary          on
	mod_gzip_minimum_file_size  500
	mod_gzip_maximum_file_size  500000
	mod_gzip_maximum_inmem_size 100000
	mod_gzip_keep_workfiles     no
	mod_gzip_temp_dir           /tmp
	mod_gzip_item_include       file \.html$
	mod_gzip_item_include       file \.htm$
	mod_gzip_item_include       file \.jsp$
	mod_gzip_item_include       file \.php$
	mod_gzip_item_include       file \.php3$
	mod_gzip_item_include       file \.pl$
	mod_gzip_item_include       file \.epl$
	mod_gzip_item_include       file \.txt$
	mod_gzip_item_include       file \.cgi$
	mod_gzip_item_include       mime ^text/
	mod_gzip_item_include       mime ^application/x-httpd-php
	mod_gzip_item_include       mime ^httpd/unix-directory$
	mod_gzip_item_include       handler ^perl-script$
	mod_gzip_item_include       handler ^cgi-script$
	mod_gzip_item_include       handler ^server-status$
	mod_gzip_item_include       handler ^server-info$
	mod_gzip_item_include       handler "jserv-servlet"
	mod_gzip_item_exclude       reqheader  "User-agent: Mozilla/4.0[678]"
	mod_gzip_item_exclude       file \.css$
	mod_gzip_item_exclude       file \.js$
	mod_gzip_item_exclude       file \.wml$
	mod_gzip_item_exclude       mime ^image/
</IfModule>
EOF

%build
%{__make} %{?_smp_mflags} \
	APXS="%{_sbindir}/apxs"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mod_gzip.so %{buildroot}%{_libdir}/apache/mod_gzip.so
%{__install} -Dp -m0644 mod_gzip.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_gzip.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog docs/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_gzip.conf
%{_libdir}/apache/mod_gzip.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.26-0.1a.2
- Rebuild for Fedora Core 5.

* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 1.3.26-0.1a
- Initial package. (using DAR)

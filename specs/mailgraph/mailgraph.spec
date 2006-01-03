# $Id$
# Authority: nac

Summary:        RRDtool-based mail graphing tool
Name:           mailgraph
Version:        1.11
Release:        1.0
License:        GPL
Group:          Applications/System
Source:         http://people.ee.ethz.ch/~dws/software/mailgraph/pub/mailgraph-1.11.tar.gz
Source1:        mailgraph.httpd-conf
Patch:          mailgraph.patch
URL:            http://people.ee.ethz.ch/~dws/software/mailgraph/  
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       perl(File::Tail)

%description

Mailgraph is a very simple mail statistics RRDtool frontend for Postfix
and Sendmail that produces daily, weekly, monthly and yearly graphs of
received/sent and bounced/rejected mail.

%prep
%setup
%patch

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_localstatedir}/lib/%{name}/rrd/
%{__install} -d %{buildroot}%{_localstatedir}/lib/%{name}/img/
%{__install} -d %{buildroot}%{_libdir}/%{name}/cgi/
%{__install} -d %{buildroot}%{_sysconfdir}/rc.d/init.d/
%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig/
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/conf.d/

%{__install} mailgraph.pl %{buildroot}%{_libdir}/%{name}/
%{__install} mailgraph.cgi %{buildroot}%{_libdir}/%{name}/cgi/
%{__install} mailgraph-init %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
%{__install} mailgraph.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/mailgraph.conf.example

%clean
%{__rm} -rf %{buildroot}

%postun
if [ $1 -eq 0 ] ; then \
	/sbin/chkconfig --del %{name}
fi

%post
if [ $1 -eq 1 ] ; then \
	/sbin/chkconfig --add %{name}
fi

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README

%{_libdir}/%{name}/
%{_localstatedir}/lib/%{name}/rrd/
%attr(755,httpd,httpd) %{_localstatedir}/lib/%{name}/img/
%{_sysconfdir}/rc.d/init.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*


%changelog
* Fri Jul 29 2005 Wil Cooley <wcooley@nakedape.cc> - 1.11-1.0
- Initial package creation
